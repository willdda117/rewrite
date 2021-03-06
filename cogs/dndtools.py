import logging

from backends.encounter_gen import calculate_xp, load_monsters, create_monster_list, encounter_gen, final_encounter
from discord.ext.commands import Cog, command

log = logging.getLogger('bot.' + __name__)


class DndTools(Cog, name='D&D Tools'):
    """These are all the commands that function as tools while playing D&D."""
    def __init__(self, bot):
        self.bot = bot

    @command(name='currency')
    async def currency_command(self, ctx, *coins):
        """Recalculates the given currency into the highest possible value.
        ;currency 500sp will recalculate it into 5pp.
        Multiple currencies can be given."""
        cp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "cp"])
        sp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "sp"])
        ep = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "ep"])
        gp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "gp"])
        pp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "pp"])
        total = (cp * 1) + (sp * 10) + (ep * 50) + (gp * 100) + (pp * 1000)
        cp = total % 10
        total = total // 10
        sp = total % 10
        total = total // 10
        gp = total % 10
        total = total // 10
        pp = total
        return await ctx.send(f"Recalculated your currency into: {str(cp)}cp, {str(sp)}sp, {str(gp)}gp and {str(pp)}pp")

    @command(name='encounter')
    async def encounter_command(self, ctx, psize, plevel, difficulty, environment):
        """Generates a random encounter based on the users inputs.
        The user can input: the size of the party, the average level of the party,
        the difficulty of the encounter and the environment it takes place in."""
        difficulties = ['easy', 'medium', 'difficult', 'deadly']
        environments = ['city', 'dungeon', 'forest', 'nature', 'other plane', 'underground', 'water']
        try:
            psize = int(psize)
            plevel = int(plevel)
        except ValueError:
            return await ctx.send('Party size and level must be numbers.')
        if plevel > 20:
            return await ctx.send('Party level must be a number between 1 and 20.')
        if psize > 10:
            return await ctx.send('Party size must be a number between 1 and 20.')
        if difficulty in difficulties:
            if difficulty == 'easy':
                difficulty = 1
            if difficulty == 'medium':
                difficulty = 2
            if difficulty == 'difficult':
                difficulty = 3
            if difficulty == 'deadly':
                difficulty = 4
        else:
            return await ctx.send(f"Please choose from 1 of the following difficulties: **{' - '.join(difficulties)}**")
        if environment not in environments:
            return await ctx.send(f"Please choose from 1 of the following environments: **{' - '.join(environments)}**")
        xp = calculate_xp(plevel, difficulty, psize)
        monsterdata = load_monsters()
        possiblemonsters = create_monster_list(monsterdata, environment)
        encounter = encounter_gen(possiblemonsters, xp)
        final = final_encounter(encounter, xp)
        return await ctx.send(final)


def setup(bot):
    bot.add_cog(DndTools(bot))
    log.debug('Reddit cog loaded.')
