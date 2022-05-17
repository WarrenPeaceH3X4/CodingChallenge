def timeConversion(s):
    # Write your code here
    s = s.split(':')
    hr, mt, sc = s[0], s[1], s[2]
    ampm = sc[2:]
    sc = sc[:2]    
    if ampm == 'PM' and hr != '12':
        hr = str(int(hr) + 12)
    elif ampm == 'AM' and hr == '12':
        hr = '00'
    return f"{hr}:{mt}:{sc}"