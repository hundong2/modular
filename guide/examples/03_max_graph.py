"""CPU에서 두 Float32 vector를 더하는 최소 MAX Graph 실습."""

import numpy as np
from max.driver import CPU, Buffer
from max.dtype import DType
from max.engine import InferenceSession
from max.graph import DeviceRef, Graph, TensorType


def main() -> None:
    """Graph를 compile하고 입력 buffer 두 개를 실행합니다."""
    device = CPU()
    input_type = TensorType(
        dtype=DType.float32,
        shape=(4,),
        device=DeviceRef.from_device(device),
    )

    with Graph(
        "guide_vector_add", input_types=(input_type, input_type)
    ) as graph:
        lhs = graph.inputs[0].tensor
        rhs = graph.inputs[1].tensor
        graph.output(lhs + rhs)

    model = InferenceSession(devices=[device]).load(graph)
    lhs_values = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
    rhs_values = np.array([10.0, 20.0, 30.0, 40.0], dtype=np.float32)
    lhs_buffer = Buffer.from_numpy(lhs_values).to(device)
    rhs_buffer = Buffer.from_numpy(rhs_values).to(device)

    result = model.execute(lhs_buffer, rhs_buffer)[0]
    assert isinstance(result, Buffer)
    actual = result.to(CPU()).to_numpy()
    expected = lhs_values + rhs_values
    np.testing.assert_allclose(actual, expected)
    print("result:", actual)


if __name__ == "__main__":
    main()
