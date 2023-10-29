def validate_dict(rules, dict):
    for key, prefix, middle, suffix in rules:
        if key not in dict:
            return False
        value = dict[key]
        if value.startswith(prefix) and value.endswith(suffix) and middle in value[1:-1]:
            return True
        else: return False

s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d={"key1": "come inside, it's too cold out", "key3": "this is not valid"}

print(validate_dict(s, d))