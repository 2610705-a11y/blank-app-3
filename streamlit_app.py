import streamlit as st

st.title("🧳 가족 수하물 무게 체크 프로그램")
st.markdown("---")

num_family = st.number_input(
    "가족의 인원을 입력해 주세요:", min_value=1, value=1, step=1
)

st.markdown("### 📦 짐 무게 입력")
baggage_weights = []

for i in range(num_family):
    weight = st.number_input(
        f"({i+1}번째 짐의 무게를 입력해주세요 (kg):",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key=f"baggage_{i}",
    )
    baggage_weights.append(weight)

st.markdown("---")

if st.button("무게 확인 및 결과 보기"):
    total_weight = sum(baggage_weights)
    max_allowed_weight = num_family * 40

    st.write(f"**총 수하물 무게:** {total_weight:.1f} kg")
    st.write(f"**허용 수하물 무게:** {max_allowed_weight} kg")

    if total_weight <= max_allowed_weight:
        st.success("완료되었습니다.")
    else:
        st.warning(f"허용 무게({max_allowed_weight}kg)를 초과했습니다.")
        st.session_state["show_extra_charge"] = True

if st.session_state.get("show_extra_charge", False):
    st.markdown("### 💰 추가 요금 확인")
    pay_extra = st.selectbox(
        "추가요금을 지불하시겠습니까?", ["선택하세요", "네", "아니오"]
    )

    if pay_extra == "네":
        st.success("완료되었습니다.")
    elif pay_extra == "아니오":
        st.error("죄송합니다.")