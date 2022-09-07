def action_check(actions: str):
    """Maybe user wrote wrong digit or even a letter"""
    for i in range(1, 6 + 1):
        actions = actions.replace(f'{i}', '')
    print(actions)
    if actions == '':
        return True
    return False





if __name__ == '__main__':
    print('You cant run this file as main')
