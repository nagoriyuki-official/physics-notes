# 自由落体运动计算：距离 h = 1/2 * g * t^2
g = 9.8  # 重力加速度 (m/s^2)

def falling_distance(t):
    """返回自由落体 t 秒后下落的距离（米）"""
    return 0.5 * g * t * t

if __name__ == "__main__":
    for t in [1, 2, 3, 5, 10]:
        print(f"{t} 秒后下落 {falling_distance(t):.1f} 米")
