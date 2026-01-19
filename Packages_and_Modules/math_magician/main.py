from geometry_lib.shapes2d import circle
from geometry_lib.shapes3d import cube

def run():
    print("--- Math Magician Tool ---")
    
    # Test 2D
    r = 5
    print(f"Circle (r={r}) Area: {circle.area(r):.2f}")
    
    # Test 3D
    side = 3
    print(f"Cube (side={side}) Volume: {cube.volume(side)}")

if __name__ == "__main__":
    run()
