# file = open("/Users/tim/Desktop/mess/file creation/struct_impl.rs")
# content = file.read()
# # print(content)
# file = open("/Users/tim/Desktop/mess/file creation/main.rs", "a")
# file.write(content)
# file.close()


struct_name = "Contract"
data = {
    "account_list": "UnorderedMap<AccountId, Balance>",
    "pool": "u32",
    "top_accounts": "UnorderedMap<AccountId, Balance>",
}
default_data = {
    "account_list": "UnorderedMap::new(b\"a\".to_vec())",
    "pool": "30",
    "top_accounts": "UnorderedMap::new(b\"t\".to_vec())",
}


from utils import *

def main():
    struct_init(struct_name, data)
    struct_impl_default(struct_name, default_data)
    contract_impl(struct_name)
    assemble()

    clear()


main()
