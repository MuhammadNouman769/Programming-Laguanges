import dis


# Ek simple function
def add_numbers(a, b):
    result = a + b
    return result


# Disassembler module ke zariye is function ka bytecode check karein
print("--- BYTECODE INSTRUCTIONS ---")
dis.dis(add_numbers)