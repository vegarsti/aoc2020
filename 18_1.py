import subprocess

# In the J programming language, the precedence is the reverse of the precedence in this problem.
# Evaluate the expressions by reversing each string and running it in J.

with open("input/18.txt", "r") as f:
    lines = f.readlines()
j_program = "18_1.ijs"
with open(j_program, "w") as f:
    for line in lines:
        line_ = line.strip()[::-1].replace(")", "#").replace("(", ")").replace("#", "(")
        f.write(f"echo {line_}\n")
    f.write("exit ''")
j_output = subprocess.check_output(["jconsole", j_program]).decode("utf-8").strip()
nums = (int(i) for i in j_output.split("\n"))
print(sum(nums))
