import sys
import os
import time

# --- 关键：把 .pyd 文件所在的目录加入 Python 搜索路径 ---
# 假设你的 .pyd 在 ../x64/Release 目录下
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../x64/Release'))
sys.path.append(dll_path)

# --- 见证奇迹的时刻 ---
# 现在可以像导入普通 Python 库一样导入它了！
try:
    import Cpp_Optimization_Sandbox as my_cpp_lib
except ImportError as e:
    print(f"导入失败: {e}")
    print(f"请检查路径: {dll_path}")
    print("并确保你生成的是 Release 版本且后缀是 .pyd")
    exit()

# 看看它的文档
print(f"模块文档: {my_cpp_lib.__doc__}")

# 调用函数
ITERATIONS = 10_000_000
print(f"C++ 开始计算 (次数: {ITERATIONS})...")
start = time.time()

# 直接调用！不需要 argtypes，不需要 restype，直接传 int，返回 double
result = my_cpp_lib.calculate_pi(ITERATIONS)

end = time.time()
print(f"结果: {result}")
print(f"耗时: {end - start:.4f} 秒")