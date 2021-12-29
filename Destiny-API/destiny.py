import pydest
import asyncio

DESTINY2_URL = 'https://www.bungie.net/Platform/Destiny2/'
platforms = {'XBOX': 1, 'PLAYSTATION': 2, 'PC': 3}


async def update_account_stats(account):
    """You will need to add your api key!"""
    destiny = pydest.Pydest('b7f519458a574d0594d9d6223f56be5a')

    platform = None
    while not platform:
        user_input = 'xbox'
        if user_input.upper() in platforms.keys():
            platform = platforms.get(user_input.upper())
        else:
            print('Invalid platform.')

    username = 'philiplgelinas#6699'
    res = await destiny.api.search_destiny_player(platform, username)

    if res['ErrorCode'] == 1 and len(res['Response']) > 0:
        membershipId = res['Response'][0]['membershipId']
        raid_clears = await destiny.api.get_raid_clears(membershipId)
    else:
        print("Could not locate player.")

    activity1 = await destiny.decode_hash(119944200, 'DestinyActivityDefinition')
    await destiny.update_manifest()

    print("Activity Name: {}".format(activity1['displayProperties']['name']))
    print("Description: {}".format(activity1['displayProperties']['description']))

    await destiny.close()
