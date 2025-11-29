popData = { 'CA': 39.5, 'TX': 30.0, 'FL': 22.2, 'NY': 19.8, 'PA': 13.0, 'IL': 12.8, 'OH': 11.8,
            'GA': 10.9, 'NC': 10.7, 'MI': 10.1}

def retrieve_pop(region_code: str , data_dict: dict):
    # we check if the reg_code
    if region_code in data_dict:
        return data_dict[region_code]
    else:
        print('Region code not found')
        return None

def main():
    boolean_flag = True

    # check to see if there have been error
    while boolean_flag == True:
        user_region_code = input('Please enter a country code: ')
        retrieved_data = retrieve_pop(user_region_code, popData)

        if retrieved_data is None:
            print(f'Error: {user_region_code} is not recognized. Valid codes: {popData.keys()}')
            retry_input = input('Would you like to try again? (yes/no): ')

            if retry_input == 'yes' or retry_input == 'y':
                continue
            elif retry_input == 'no' or retry_input == 'n':
                print('Program terminated.')
                boolean_flag = False
            else:
                print('Wrong input. Try again.')
                break
        else:
            print(f'{user_region_code} population = {retrieved_data}')
            boolean_flag = False

main()


