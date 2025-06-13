# brawlstars_game.py
import streamlit as st
import random

# 브롤러 데이터
brawlers = [
    {"name": "Shelly", "hp": 3800, "attack": 500},
    {"name": "Colt", "hp": 2800, "attack": 600},
    {"name": "Bull", "hp": 5200, "attack": 400},
    {"name": "Poco", "hp": 4000, "attack": 300},
]

st.title("💥 브롤스타즈 배틀 시뮬레이터")

# 플레이어 브롤러 선택
player_brawler_name = st.selectbox("내 브롤러를 선택하세요", [b["name"] for b in brawlers])
player_brawler = next(b for b in brawlers if b["name"] == player_brawler_name)

# 컴퓨터 브롤러 선택
enemy_brawler = random.choice(brawlers)

if st.button("⚔️ 배틀 시작"):
    st.subheader(f"🥷 당신의 브롤러: {player_brawler['name']} (HP: {player_brawler['hp']}, ATK: {player_brawler['attack']})")
    st.subheader(f"🤖 적 브롤러: {enemy_brawler['name']} (HP: {enemy_brawler['hp']}, ATK: {enemy_brawler['attack']})")

    # 전투 시뮬레이션
    player_hp = player_brawler["hp"]
    enemy_hp = enemy_brawler["hp"]

    rounds = 0
    battle_log = []

    while player_hp > 0 and enemy_hp > 0:
        rounds += 1
        enemy_hp -= player_brawler["attack"]
        player_hp -= enemy_brawler["attack"]
        battle_log.append(f"{rounds}턴: {player_brawler['name']}이(가) 공격 → 적 HP: {max(enemy_hp, 0)}")
        battle_log.append(f"{rounds}턴: {enemy_brawler['name']}이(가) 반격 → 내 HP: {max(player_hp, 0)}")

    # 결과 출력
    for log in battle_log:
        st.write(log)

    if player_hp > 0 and enemy_hp <= 0:
        st.success("🎉 승리!")
    elif enemy_hp > 0 and player_hp <= 0:
        st.error("💀 패배...")
    else:
        st.warning("⚖️ 무승부!")


