from xml.dom.expatbuilder import FilterVisibilityController
def run(can_fly: bool, is_human: bool, has_mask: bool) -> str:
    # TODO
    if can_fly and is_human and has_mask:
        character = 'Ironman'
    elif can_fly and is_human and not has_mask:
        character = 'Captain Marvel'
    elif can_fly and not is_human and has_mask:
        character = 'Ronan Accuser'
    elif can_fly and not is_human and not has_mask:
        character = 'Vision'
    elif not can_fly and is_human and has_mask:
        character = 'Spider-Man'
    elif not can_fly and is_human and not has_mask:
        character = 'Hulk'
    elif not can_fly and not is_human and has_mask:
        character = 'Black Bolt'
    else:
        character = 'Thanos'

    return character


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
