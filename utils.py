
struct_init_template_path = "/Users/tim/Desktop/mess/file creation/templates/struct_init.rs"
struct_impl_default_template_path = "/Users/tim/Desktop/mess/file creation/templates/struct_impl_default.rs"
contract_impl_template_path = "/Users/tim/Desktop/mess/file creation/templates/contract_impl.rs"
struct_init_path = "/Users/tim/Desktop/mess/file creation/struct_init.rs"
struct_impl_default_path = "/Users/tim/Desktop/mess/file creation/struct_impl_default.rs"
contract_impl_path = "/Users/tim/Desktop/mess/file creation/contract_impl.rs"
header_path = "/Users/tim/Desktop/mess/file creation/header.rs"

result_path = "/Users/tim/Desktop/mess/file creation/result.rs"

func1_path = "/Users/tim/Desktop/mess/file creation/functions/func1.rs"
func2_path = "/Users/tim/Desktop/mess/file creation/functions/func2.rs"

tab = "    "
new_line = "\n"

def header():
    header = open(header_path).read()
    open(result_path, 'a').write(header)

def struct_init(struct_name, data):
    file = open(struct_init_template_path)
    template = file.read()
    file = open(struct_init_path, "a")
    file.write(template)
    # 
    file = open(struct_init_path, "a")
    file.write(" " + struct_name + " {" + new_line + tab)
    for key, val in data.items():
        if key == list(data)[-1]:
            file.write(key + ": " + val + "," + new_line + "}" + new_line)
        else:
            file.write(key + ": " + val + "," + new_line + tab)
    file.close()

def struct_impl_default(struct_name, data):
    file = open(struct_impl_default_template_path)
    template = file.read()
    file = open(struct_impl_default_path, "a")
    file.write(template)
    # 
    file = open(struct_impl_default_path, "a")
    file.write(" " + struct_name + " {" + new_line + tab)
    file.write("fn default() -> self {" + new_line + tab + tab + "Self " + "{ " + new_line + tab + tab + tab)
    for key, val in data.items():
        if key == list(data)[-1]:
            file.write(key + ": " + val + "," + new_line + tab + tab + "}" + new_line)
            file.write(tab + "}" + new_line)
            file.write("}" + new_line)
        else:
            file.write(key + ": " + val + "," + new_line + tab + tab + tab)
    file.close()

def contract_impl(struct_name):
    file = open(contract_impl_template_path)
    template = file.read()
    file = open(contract_impl_path, "a")
    file.write(template)
    # 
    file = open(contract_impl_path, "a")
    file.write(" " + struct_name + " {" + new_line + tab)

    func1 = open(func1_path).read()
    file.write(func1 + new_line )
    
    func2 = open(func2_path).read()
    file.write(func2 + new_line )

    file.write("}" + new_line)
    file.close()

def assemble():
    result = open(result_path, "a")
    header()
    init = open(struct_init_path).read()
    result.write(init)
    default_struct = open(struct_impl_default_path).read()
    result.write(default_struct)
    contract_impl = open(contract_impl_path).read()
    result.write(contract_impl)
    result.close()

def clear():
    open(struct_init_path, 'w').close()
    open(struct_impl_default_path, 'w').close()
    open(contract_impl_path, 'w').close()
    open(result_path, 'w').close()
