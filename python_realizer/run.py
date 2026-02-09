import ctypes
import time
import os
import random

# ==========================================
# 1. 加载 C++ DLL (核心步骤)
# ==========================================
# 自动定位 DLL 路径：从当前脚本位置往上找 ../x64/Release/xxx.dll
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../x64/Release/Cpp_Optimization_Sandbox.dll'))

print(f"正在加载 DLL: {dll_path} ...")
try:
    # 加载动态库
    cpp_lib = ctypes.CDLL(dll_path)
    
    # 【关键】告诉 Python，C++ 函数的参数和返回值是什么类型
    # C++ 签名: double calculate_pi(int iterations)
    cpp_lib.calculate_pi.argtypes = [ctypes.c_int]    # 参数是 int
    cpp_lib.calculate_pi.restype = ctypes.c_double    # 返回值是 double
    
    print("DLL 加载成功！\n")
except FileNotFoundError:
    print("❌ 找不到 DLL 文件！请检查路径或确保你已经 Build 成功。")
    exit()

# 2. 定义纯 Python 版本的算法 (用来做陪练)

def python_calculate_pi(iterations):
    inside_circle = 0
    for _ in range(iterations):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            inside_circle += 1
    return 4.0 * inside_circle / iterations


ITERATIONS = 10_000_000  # 跑 1000 万次循环 (可以根据电脑性能调整)

print(f"开始测试, 循环次数: {ITERATIONS}")

# --- 选手 1: Python ---
print("Python计算中")
start_py = time.time()
pi_py = python_calculate_pi(ITERATIONS)
end_py = time.time()
time_py = end_py - start_py
print(f"Python\t结果: {pi_py:.6f}, 耗时: {time_py:.4f} 秒")


print("C++计算中")
start_cpp = time.time()
# 直接调用 DLL 里的函数
pi_cpp = cpp_lib.calculate_pi(ITERATIONS)
end_cpp = time.time()
time_cpp = end_cpp - start_cpp
print(f"C++\t结果: {pi_cpp:.6f}, 耗时: {time_cpp:.4f} 秒")