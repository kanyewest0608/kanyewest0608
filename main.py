# shooting_game.py
import streamlit as st
import random

st.set_page_config(page_title="브롤스타즈 슈팅 게임 🔫")

st.title("🔫 브롤스타즈 턴제 슈팅 게임")
st.markdown("플레이어와 적이 서로 공격하며 승부를 가릅니다!")

# 초기 설정
if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.distance = 3  # 1이 가까움, 5는 멀다
    st.session_state.log = []

# 상태 표시
st.metric("🧍 내 체력", st.session_state.player_hp)
st.metric("🤖 적 체력", st.session_state.enemy_hp)
st.text(f"📏 현재 거리: {st.session_state.distance}칸")

# 행동 선택
action = st.selectbox("행동을 선택하세요", ["앞으로 이동", "공격", "회복"])

if st.button("▶️ 실행"):
    log = ""

    # 플레이어 행동
    if action == "앞으로 이동":
        if st.session_state.distance > 1:
            st.session_state.distance -= 1
            log += "🧍 당신이 앞으로 한 칸 이동했습니다.\n"
        else:
            log += "❌ 이미 최대한 가까움!\n"
    elif action == "공격":
        if st.session_state.distance <= 2:
            dmg = random.randint(10, 30)
            st.session_state.enemy_hp -= dmg
            log += f"💥 공격 성공! 적에게 {dmg} 데미지를 입혔습니다.\n"
        else:
            log += "😅 너무 멀어서 공격 실패!\n"
    elif action == "회복":
        heal = random.randint(5, 20)
        st.session_state.player_hp += heal
        log += f"💚 체력을 {heal} 회복했습니다.\n"

    # 적 행동
    enemy_action = random.choice(["공격", "대기"])
    if enemy_action == "공격" and st.session_state.distance <= 2:
        dmg = random.randint(5, 25)
        st.session_state.player_hp -= dmg
        log += f"💢 적이 공격했습니다! 당신은 {dmg} 데미지를 입었습니다.\n"
    elif enemy_action == "공격":
        log += "😎 적이 공격하려 했지만 너무 멀었습니다.\n"
    else:
        log += "😴 적이 대기 중입니다.\n"

    # 로그 저장
    st.session_state.log.append(log)

# 전투 로그 출력
st.subheader("📜 전투 로그")
for l in reversed(st.session_state.log[-5:]):
    st.text(l)

# 게임 종료 조건
if st.session_state.player_hp <= 0:
    st.error("💀 게임 오버! 당신이 패배했습니다.")
    if st.button("🔄 다시 시작"):
        st.session_state.player_hp = 100
        st.session_state.enemy_hp = 100
        st.session_state.distance = 3
        st.session_state.log = []

elif st.session_state.enemy_hp <= 0:
    st.success("🎉 승리! 적을 처치했습니다.")
    if st.button("🔁 다시 시작"):
        st.session_state.player_hp = 100
        st.session_state.enemy_hp = 100
        st.session_state.distance = 3
        st.session_state.log = []

