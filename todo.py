import json, os

FILE = "todos.json"
todos = json.load(open(FILE, "r", encoding="utf-8")) if os.path.exists(FILE) else []

while True:
    print("\n--- [1] 목록 [2] 추가 [3] 완료/삭제 [4] 종료 ---")
    cmd = input("선택: ")
    
    if cmd == "1":
        print("\n".join(f"{i+1}. {t}" for i, t in enumerate(todos)) or "할 일이 없습니다.")
    elif cmd == "2":
        t = input("추가할 할 일: ")
        todos.append(t)
        json.dump(todos, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    elif cmd == "3":
        idx = int(input("완료할 번호: ")) - 1
        if 0 <= idx < len(todos):
            removed = todos.pop(idx)
            json.dump(todos, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print(f"'{removed}' 완료 처리되었습니다.")
    elif cmd == "4":
        break
