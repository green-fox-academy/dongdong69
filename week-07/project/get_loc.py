import postcodes_io_api

def get_loc(postcode):

    api  = postcodes_io_api.Api(debug_http=True)
    data = api.get_postcode(postcode)
    return (data['result']['latitude'], data['result']['longitude'], data['result']['postcode'].split()[0])


if __name__ == '__main__':
    print(get_loc('SW112EF'))