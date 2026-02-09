import sys
import os
import time

dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../x64/Release'))
sys.path.append(dll_path)

try:
    import Cpp_Optimization_Sandbox as my_cpp_lib
except ImportError as e:
    print(f"导入失败: {e}")
    print(f"请检查路径: {dll_path}")
    print("并确保你生成的是 Release 版本且后缀是 .pyd")
    exit()

print(f"模块文档: {my_cpp_lib.__doc__}")

ITERATIONS = 10_000_000
print(f"C++ 开始计算 (次数: {ITERATIONS})...")
start = time.time()

result = my_cpp_lib.calculate_pi(ITERATIONS)

end = time.time()
print(f"结果: {result}")
print(f"耗时: {end - start:.4f} 秒")