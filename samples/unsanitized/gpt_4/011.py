Sure, here is the completed Python function:

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
```