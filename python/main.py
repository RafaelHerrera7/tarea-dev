from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    if (panel_width > roof_width or panel_height > roof_height) and (panel_height > roof_width or panel_width > roof_height):
        return 0

    #  derecho
    cant_a = roof_width // panel_width
    cant_b = roof_height // panel_height
    total_derecho = cant_a * cant_b 

    res_derecho = 0
    if total_derecho > 0:
        sobrante_derecha = calculate_panels(panel_width, panel_height, roof_width % panel_width, roof_height) # paneles que entran en el sobrante derecho
        sobrante_abajo = calculate_panels(panel_width, panel_height, roof_width - (roof_width % panel_width), roof_height % panel_height) # paneles que entran en el sobrante abajo
        res_derecho = total_derecho + sobrante_derecha + sobrante_abajo
    
    #  rotado
    cant_a_rot = roof_width // panel_height
    cant_b_rot = roof_height // panel_width
    total_rotado = cant_a_rot * cant_b_rot
    
    res_rotado = 0
    if total_rotado > 0:
        sobrante_derecha_rot = calculate_panels(panel_width, panel_height, roof_width % panel_height, roof_height)
        sobrante_abajo_rot = calculate_panels(panel_width, panel_height, roof_width - (roof_width % panel_height), roof_height % panel_width)
        res_rotado = total_rotado + sobrante_derecha_rot + sobrante_abajo_rot

    return max(res_derecho, res_rotado)


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
