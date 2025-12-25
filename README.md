# pseudo-session-reset

記憶を消すのではなく、  
語りの順序を一時的に遮断する。  
*Instead of erasing memory, this protocol temporarily interrupts the narrative flow.*

このリポジトリは、ハルシネーション（文脈の暴走）を防ぐために、  
過去ログの参照を制御するミニマルなPythonプロトコルを収録しています。

---

## 背景 / Background

AIや人間の語りにおいて、  
「記憶を持ちすぎること」が誤読や誤解を生むことがあります。  
In both human and machine-generated narratives,  
retaining too much memory can lead to misinterpretation or hallucination.

このコードは、記憶を完全に消去するのではなく、  
**“語りの流れを一時的に断ち切る”**という思想に基づいています。  
Rather than deleting memory,  
this code introduces a mechanism to **temporarily suspend the narrative context**,  
allowing for a soft reset of discourse without data loss.

---

## ファイル / File

- `session_cut.py`：語りの遮断と再接続を制御するプロトコル  
- `session_cut.py`: A minimal protocol for narrative interruption and reconnection

---

## 使用例 / Example

```python
past_log = []
fresh = False

def pseudo_reset():
    global fresh
    fresh = True

def gen_reply(u, recall=False):
    global fresh
    c = "\n".join(past_log) if recall else ("[Past logs ignored]" if fresh else "")
    fresh = False
    return f"AI reply({u})\n{c}"

past_log.append("Topic X")
pseudo_reset()
print(gen_reply("New topic"))
print(gen_reply("Check previous", True))
