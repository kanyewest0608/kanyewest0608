# text_rpg_game.py
import streamlit as st
import random

st.set_page_config(page_title="텍스트 RPG 🧝‍♀️")

st.title("🗺️ Streamlit 텍스트 RPG")

# 초기 상태 설정
if "hp" not in st.session_state:
    st.session_state.hp = 100
    st.session_state.gold = 50
    st.session_state.stage = "start"
    st.session_state.log = []

# 상태 표시
st.markdown(f"**❤️ 체력:** {st.session_state.hp} / 100")
st.markdown(f"**🪙 골드:** {st.session_state.gold}")
st.markdown("---")

def battle():
    enemy_hp = 40
    log = ""
    while enemy_hp > 0 and st.session_state.hp > 0:
        player_dmg = random.randint(10, 20)
        enemy_dmg = random.randint(5, 15)
        enemy_hp -= player_dmg
        st.session_state.hp -= enemy_dmg
        log += f"🔪 당신이 {player_dmg} 데미지를 입혔고, 적에게 {enemy_dmg} 데미지를 받았습니다.\n"
    if st.session_state.hp > 0:
        reward = random.randint(10, 30)
        st.session_state.gold += reward
        log += f"🎉 승리! {reward}골드를 얻었습니다."
        st.session_state.stage = "crossroad"
    else:
        log += "💀 당신은 쓰러졌습니다..."
        st.session_state.stage = "dead"
    return log

# 스토리 분기
if st.session_state.stage == "start":
    st.write("깊은 숲속에서 눈을 뜬 당신은 길이 두 갈래로 나뉜 것을 발견합니다.")
    choice = st.radio("어디로 갈까요?", ["왼쪽 길", "오른쪽 길"])
    if st.button("🚶 이동"):
        if choice == "왼쪽 길":
            st.session_state.stage = "battle"
        else:
            st.session_state.stage = "merchant"
        st.rerun()

elif st.session_state.stage == "battle":
    st.write("⚔️ 당신은 길을 걷다가 몬스터와 마주쳤습니다!")
    if st.button("전투 시작!"):
        result = battle()
        st.session_state.log.append(result)
        st.rerun()

elif st.session_state.stage == "merchant":
    st.write("🧙‍♂️ 상인을 만났습니다. 포션(20골드)을 구매할 수 있습니다.")
    if st.button("💰 포션 구매 (20골드)"):
        if st.session_state.gold >= 20:
            st.session_state.gold -= 20
            st.session_state.hp = min(100, st.session_state.hp + 30)
            st.success("체력을 30 회복했습니다!")
        else:
            st.error("골드가 부족합니다!")
    if st.button("계속 이동"):
        st.session_state.stage = "crossroad"
        st.rerun()

elif st.session_state.stage == "crossroad":
    st.write("⛰️ 또 다른 갈림길이 나왔습니다. 여정을 계속할까요?")
    next_choice = st.radio("다음 목적지", ["더 깊은 숲", "마을로 귀환"])
    if st.button("이동!"):
        if next_choice == "더 깊은 숲":
            st.session_state.stage = "battle"
        else:
            st.success("🏡 마을에 도착해 퀘스트를 완료했습니다!")
            st.session_state.hp = 100
            st.session_state.stage = "start"
        st.rerun()

elif st.session_state.stage == "dead":
    st.error("☠️ 게임 오버!")
    if st.button("🔁 다시 시작"):
        st.session_state.hp = 100
        st.session_state.gold = 50
        st.session_state.stage = "start"
        st.session_state.log = []
        st.rerun()

# 전투 로그 출력
if st.session_state.log:
    st.subheader("📜 로그")
    for entry in reversed(st.session_state.log[-3:]):
        st.text(entry)
