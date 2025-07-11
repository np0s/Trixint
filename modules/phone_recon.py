import phonenumbers
from phonenumbers import geocoder, carrier, number_type, PhoneNumberType

PHONENUMBER_TYPE_NAMES = {
    PhoneNumberType.FIXED_LINE: 'FIXED_LINE',
    PhoneNumberType.MOBILE: 'MOBILE',
    PhoneNumberType.FIXED_LINE_OR_MOBILE: 'FIXED_LINE_OR_MOBILE',
    PhoneNumberType.TOLL_FREE: 'TOLL_FREE',
    PhoneNumberType.PREMIUM_RATE: 'PREMIUM_RATE',
    PhoneNumberType.SHARED_COST: 'SHARED_COST',
    PhoneNumberType.VOIP: 'VOIP',
    PhoneNumberType.PERSONAL_NUMBER: 'PERSONAL_NUMBER',
    PhoneNumberType.PAGER: 'PAGER',
    PhoneNumberType.UAN: 'UAN',
    PhoneNumberType.VOICEMAIL: 'VOICEMAIL',
    PhoneNumberType.UNKNOWN: 'UNKNOWN',
}

def parse_phone_number(number: str, region: str = None) -> dict:
    """
    Parse and validate a phone number. Returns info dict or error.
    Tries to auto-detect region if not provided and number is ambiguous.
    """
    def extract_info(parsed):
        valid = phonenumbers.is_valid_number(parsed)
        possible = phonenumbers.is_possible_number(parsed)
        country = geocoder.country_name_for_number(parsed, 'en')
        region_desc = geocoder.description_for_number(parsed, 'en')
        carrier_name = carrier.name_for_number(parsed, 'en')
        ntype = number_type(parsed)
        ntype_str = PHONENUMBER_TYPE_NAMES.get(ntype, str(ntype))
        return {
            'valid': valid,
            'possible': possible,
            'country': country,
            'region': region_desc,
            'carrier': carrier_name,
            'type': ntype_str,
            'e164': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
            'international': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            'national': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
        }
    # Try E.164 first
    try:
        parsed = phonenumbers.parse(number, None)
        if phonenumbers.is_possible_number(parsed):
            return extract_info(parsed)
    except Exception:
        pass
    # Heuristic: 10 digits starting with 7/8/9 is likely India
    digits = ''.join(filter(str.isdigit, number))
    if len(digits) == 10 and digits[0] in '789':
        default_region = 'IN'
    else:
        default_region = 'US'
    try:
        parsed = phonenumbers.parse(number, default_region)
        if phonenumbers.is_possible_number(parsed):
            return extract_info(parsed)
    except Exception as e:
        return {'error': f"Could not parse number. Please use international format (e.g. +12025550123). Details: {str(e)}"}
    return {'error': f"Could not parse number. Please use international format (e.g. +12025550123)."}

def print_phone_info(info: dict, number: str):
    print(f"\nPhone number info for: {number}\n" + "-"*40)
    if 'error' in info:
        print(f"Error: {info['error']}")
        return
    for k, v in info.items():
        print(f"{k.capitalize():15}: {v}")
    print("-"*40) 