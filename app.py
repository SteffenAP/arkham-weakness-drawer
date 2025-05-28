import streamlit as st
import numpy as np

deck_id = 4327199
all_basic_weaknesses = [['Amnesia', '01096', 'Core Set', 'https://arkhamdb.com/card/01096', 'Madness.'], ['Paranoia', '01097', 'Core Set', 'https://arkhamdb.com/card/01097', 'Madness.'], ['Haunted', '01098', 'Core Set', 'https://arkhamdb.com/card/01098', 'Curse.'], 
                        ['Psychosis', '01099', 'Core Set', 'https://arkhamdb.com/card/01099', 'Madness.'], ['Hypochondria', '01100', 'Core Set', 'https://arkhamdb.com/card/01100', 'Madness.'], ['Mob Enforcer', '01101', 'Core Set', 'https://arkhamdb.com/card/01101', 'Humanoid. Criminal.'], 
                        ['Silver Twilight Acolyte', '01102', 'Core Set', 'https://arkhamdb.com/card/01102', 'Humanoid. Cultist. Silver Twilight.'], ['Stubborn Detective', '01103', 'Core Set', 'https://arkhamdb.com/card/01103', 'Humanoid. Detective.'], 
                        ['Indebted', '02037', 'The Dunwich Legacy', 'https://arkhamdb.com/card/02037', 'Flaw.'], ['Internal Injury', '02038', 'The Dunwich Legacy', 'https://arkhamdb.com/card/02038', 'Injury.'], 
                        ['Chronophobia', '02039', 'The Dunwich Legacy', 'https://arkhamdb.com/card/02039', 'Madness.'], ['Overzealous', '03040', 'The Path to Carcosa', 'https://arkhamdb.com/card/03040', 'Flaw.'], 
                        ['Drawing the Sign', '03041', 'The Path to Carcosa', 'https://arkhamdb.com/card/03041', 'Pact. Madness.'], ['The Thing That Follows', '03042', 'The Path to Carcosa', 'https://arkhamdb.com/card/03042', 'Monster. Curse.'], 
                        ['Dark Pact', '04038', 'The Forgotten Age', 'https://arkhamdb.com/card/04038', 'Pact.'], ['Doomed', '04040', 'The Forgotten Age', 'https://arkhamdb.com/card/04040', 'Curse.'], ['The 13th Vision', '05041', 'The Circle Undone', 'https://arkhamdb.com/card/05041', 'Omen.'], 
                        ['The Tower • XVI', '05042', 'The Circle Undone', 'https://arkhamdb.com/card/05042', 'Omen. Tarot.'], ['Self-Centered', '06035', 'The Dream-Eaters', 'https://arkhamdb.com/card/06035', 'Flaw.'], 
                        ['Kleptomania', '06036', 'The Dream-Eaters', 'https://arkhamdb.com/card/06036', 'Madness. Talent.'], ['Narcolepsy', '06037', 'The Dream-Eaters', 'https://arkhamdb.com/card/06037', 'Madness.'], 
                        ['Your Worst Nightmare', '06038', 'The Dream-Eaters', 'https://arkhamdb.com/card/06038', 'Monster.'], ['Accursed Follower', '07038', 'The Innsmouth Conspiracy', 'https://arkhamdb.com/card/07038', 'Humanoid. Cultist. Cursed.'], 
                        ['Dread Curse', '07039', 'The Innsmouth Conspiracy', 'https://arkhamdb.com/card/07039', 'Curse.'], ['Day of Reckoning', '07040', 'The Innsmouth Conspiracy', 'https://arkhamdb.com/card/07040', 'Endtimes.'], 
                        ['Arm Injury', '08130', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08130', 'Injury.'], ['Leg Injury', '08131', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08131', 'Injury.'], 
                        ['Panic', '08132', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08132', 'Madness.'], ['Stupor', '08133', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08133', 'Madness.'], 
                        ['Lurker in the Dark', '09124', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09124', 'Monster. Shoggoth.'], ['Quantum Paradox', '09125', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09125', 'Paradox.'], 
                        ['Pay Your Due', '09126', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09126', 'Pact.'], ['Ectoplasmic Horror', '09127', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09127', 'Monster. Geist.'], 
                        ['Underprepared', '09128', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09128', 'Blunder.'], ['Maimed Hand', '10135', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10135', 'Injury.'], 
                        ['Back Injury', '10136', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10136', 'Injury.'], ['The Silver Moth', '10137', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10137', 'Item. Relic.'], 
                        ['Vow of Drzytelech', '10138', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10138', 'Pact.'], ['Down and Out', '11126', 'The Drowned City Investigator Expansion', 'https://arkhamdb.com/card/11126', 'Hardship.'], 
                        ['Morbid Curiosity', '11127', 'The Drowned City Investigator Expansion', 'https://arkhamdb.com/card/11127', 'Flaw.'], ['Disruptive Poltergeist', '11128', 'The Drowned City Investigator Expansion', 'https://arkhamdb.com/card/11128', 'Curse.'], 
                        ['Frenzied', '11129', 'The Drowned City Investigator Expansion', 'https://arkhamdb.com/card/11129', 'Madness.'], ['Through the Gates', '51011', 'Return to the Dunwich Legacy', 'https://arkhamdb.com/card/51011', 'Pact. Mystery.'], 
                        ['Unspeakable Oath', '52011', 'Return to the Path to Carcosa', 'https://arkhamdb.com/card/52011', 'Madness. Pact.'], ['Unspeakable Oath', '52012', 'Return to the Path to Carcosa', 'https://arkhamdb.com/card/52012', 'Madness. Pact.'], 
                        ['Unspeakable Oath', '52013', 'Return to the Path to Carcosa', 'https://arkhamdb.com/card/52013', 'Madness. Pact.'], ['Dendromorphosis', '53012', 'Return to the Forgotten Age', 'https://arkhamdb.com/card/53012', 'Curse. Flora.'], 
                        ['Offer You Cannot Refuse', '53013', 'Return to the Forgotten Age', 'https://arkhamdb.com/card/53013', 'Pact.'], ['Damned', '54014', 'Return to the Circle Undone', 'https://arkhamdb.com/card/54014', 'Curse. Omen.'], 
                        ['The Devil • XV', '54015', 'Return to the Circle Undone', 'https://arkhamdb.com/card/54015', 'Omen. Tarot.'], ['Self-Destructive', '60104', 'Nathaniel Cho', 'https://arkhamdb.com/card/60104', 'Flaw.'], 
                        ['Obsessive', '60204', 'Harvey Walters', 'https://arkhamdb.com/card/60204', 'Flaw.'], ['Reckless', '60304', 'Winifred Habbamock', 'https://arkhamdb.com/card/60304', 'Flaw.'], ['Nihilism', '60404', 'Jacqueline Fine', 'https://arkhamdb.com/card/60404', 'Madness.'], 
                        ['Atychiphobia', '60504', 'Stella Clark', 'https://arkhamdb.com/card/60504', 'Madness.']]


class_expansions = ['The Forgotten Age', 'The Dream-Eaters', 'Return to the Forgotten Age', 'Stella Clark', 'The Scarlet Keys Investigator Expansion', 'Winifred Habbamock', 'Core Set', 'The Circle Undone', 'Harvey Walters', 'Return to the Dunwich Legacy', 'The Dunwich Legacy', 'Edge of the Earth Investigator Expansion', 'Return to the Path to Carcosa', 'The Feast of Hemlock Vale Investigator Expansion', 'Jacqueline Fine', 'Nathaniel Cho', 'Return to the Circle Undone', 'The Innsmouth Conspiracy', 'The Path to Carcosa', 'The Drowned City Investigator Expansion']

def display_cards(players_cards):
    for i, player_cards in enumerate(players_cards):
        st.markdown(f"### Player {i+1}")

        cols = st.columns(len(player_cards))

        for col, card in zip(cols, player_cards):
            name, _, expansion, link, _ = card
            col.markdown(
                f"""
                <div>
                    <strong>{name}</strong><br>
                    <em>{expansion}</em><br>
                    <a href="{link}" target="_blank">🔗 ArkhamDB</a>
                </div>
                """, unsafe_allow_html=True
            )

def filter_expansion(selected_sets):
    basic_weaknesses = [card for card in all_basic_weaknesses if card[2] in selected_sets]
    return basic_weaknesses

def filter_traits(cards, traits):
    traits = [t.lower().strip() for t in traits]  # Normalize input traits
    result = []
    for card in cards:
        card_traits = card[4].lower() if card[4] else ""  # Normalize card traits
        if any(trait in card_traits for trait in traits):
            result.append(card)
    return result

def draw(cards, players, pool):
    playercards = []
    drawn = np.random.choice(range(len(pool)), size=cards*players, replace=False)
    for player in range(players):
        temp = []
        for card in range(cards):
            draw = drawn[(player * cards) + card]
            temp.append(pool[draw])
        playercards.append(temp)
    return playercards

st.title("Arkham Horror Weakness Drawer")

if "selected_sets" not in st.session_state:
    st.session_state.selected_sets = class_expansions.copy()

selected_sets = st.multiselect(
    "Choose expansions to include",
    options=class_expansions,
    default=st.session_state.selected_sets,
    key="expansion_multiselect"
)

trait_input = st.text_input("Filter by traits (comma-separated, optional)", placeholder="e.g., Madness,Pact")

cards = st.number_input("Cards per player", min_value=1, max_value=6, value=1)
players = st.number_input("Number of players", min_value=1, max_value=4, value=1)

if st.button("Draw!"):
    pool = filter_expansion(selected_sets)
    if trait_input:
        traits = [t.strip() for t in trait_input.split(',')]
        pool = filter_traits(pool, traits)
    if len(pool) < cards * players:
        st.error("Not enough cards to draw from! Reduce players/cards or broaden filters.")
    else:
        results = draw(cards, players, pool)
        display_cards(results)


st.markdown(
    """
    <hr>
    <small style="color: gray;">
    Arkham Horror: The Card Game is a trademark of Fantasy Flight Games. This app is a fan-made tool and is not affiliated with or endorsed by Fantasy Flight Games. Card data provided by <a href="https://arkhamdb.com/" target="_blank">ArkhamDB</a>. 
    </small>
    """,
    unsafe_allow_html=True,
)