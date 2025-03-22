import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt


st.header("🌍FIFA World Cup🏆⚽(1990-2022)")
st.subheader("Introduction")
st.write('The FIFA World Cup is the most prestigious football (soccer) tournament in the world, held every four years for National teams. It brings together national teams from all over the globe to compete for the coveted title of World Champion. '
'The tournament has been a symbol of international unity, cultural exchange, and athletic excellence since its inception in 1930. Since its debut in 1930, it has captivated billions of fans worldwide, becoming more than just a tournament—it’s a celebration of culture, history, and passion. '
'From the historic streets of Italy in 1990 to the modern marvels of Qatar in 2022, each World Cup leaves behind unforgettable memories—thrilling victories, dramatic comebacks, and iconic players who etch their names into football legend. '
'In this dashboard, I will explore the journey of the BEST teams(winners) in the tournament through some of the years, diving into some of the countries that hosted, the teams that triumphed, the intense rivalries that unfolded between the top teams, and the matches that made us jump out of our seats (1990-2022).')

#My Data
df = pd.read_csv(r'C:\Users\pc\Desktop\AppFile\Worldcup Data.csv')

#My Sidebar Navigation
st.sidebar.title("Fifa Worldcup Dashboard⚽🏆")
page = st.sidebar.selectbox("Select a section", ["Introduction", "Data Summary", "Goals by Year", "Number of Wins by Country", "Goals Scored vs. Host Country", "Overall Winners & Runners-Up"])

if page == "Introduction":
    st.write("📊World Cup Data📊 (1990-2022)", df)

elif page == "Data Summary":
    st.subheader("📊Data Summary📊")
    st.write(df.describe())
    

elif page == "Goals by Year":
    st.write("### Goals Scored by Year⚽(1990-2022)")
    st.write('The FIFA World Cup has seen significant variations in the number of goals scored across different tournaments, reflecting changes in playing styles, tactical approaches, and tournament structures. Since 1990, the total goals scored in each edition have ranged from 115 to 172, with some tournaments witnessing high-scoring matches while others were more defensively oriented. The 1998 and 2014 World Cups both recorded 171 goals, while the 2022 edition in Qatar set a new record with 172 goals. Factors such as rule changes, team strategies, and player performances have all influenced the goal tally in each tournament shaping the excitement and unpredictability of the worlds biggest football event.')
    st.subheader('A Bar Graph of Goals Scored by Year')
    goals_by_year = df.groupby("Year")["Goals_Scored"].sum()
    fig, ax = plt.subplots()
    sns.barplot(x=goals_by_year.index, y=goals_by_year.values, ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Goals")
    st.pyplot(fig)
    st.write('The bar chart **"Goals Scored by Year"** represents the total number of goals scored in each FIFA World Cup from 1990 to 2022. The x-axis displays the tournament years, while the y-axis shows the total goals scored. The height of each bar indicates the number of goals scored in that particular year, allowing for easy comparison across tournaments. The chart reveals fluctuations in goal totals, with a noticeable low of 115 goals in 1990 and a steady increase in subsequent years. Peaks can be observed in 1998, 2014, and 2022, with the latter reaching a record-breaking 172 goals. The number of goals scored in each World Cup has varied over the years. Some tournaments have seen a higher number of goals, reflecting an era of attacking football, while others had fewer goals due to defensive strategies or competitive balance. This chart gives us a glimpse into how scoring patterns have evolved over time. This trend suggests evolving playing styles, tactical approaches, and possibly rule changes that have contributed to higher goal-scoring in recent tournaments.')
    total_goals_by_year = df.groupby("Year")["Goals_Scored"].sum()
    fig, ax = plt.subplots()
    total_goals_by_year.plot(kind='line', ax=ax)
    ax.set_title("Total Goals Scored Over Time⚽")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Goals")
    st.pyplot(fig)
    st.write('The line graph titled **"Total Goals Scored Over Time"** illustrates the progression of total goals scored in the FIFA World Cup from 1990 to 2022. The x-axis represents the tournament years, while the y-axis shows the total number of goals scored in each edition. The graph reveals a generally upward trend in goal scoring, with some fluctuations along the way. The most notable increases in goals occur in the 1998, 2014, and 2022 tournaments, each of which recorded a high number of goals. These fluctuations suggest how changes in tournament dynamics, such as rule adjustments, playing styles, and team strategies, have influenced goal-scoring patterns over the years. The line graph effectively highlights the overall shift toward more attacking play in recent World Cups, reflecting the evolving nature of international football.')

elif page == "Number of Wins by Country":
    st.write("## 🏆Number of Wins by Country🏆 (1990-2022)")
    st.write('The FIFA World Cup from 1990 to 2022 has seen a diverse range of nations claiming the prestigious title, showcasing football dominance across different eras. During this period, five countries—West Germany, Brazil, France, Italy, and Spain—have lifted the trophy, with Brazil and France securing multiple victories. Each tournament reflects shifts in global football power, tactical innovations, and the emergence of new footballing dynasties. The distribution of wins highlights the competitiveness of international football, where traditional powerhouses and rising teams continually battle for supremacy on the world stage.')
    wins_by_country = df["Winner"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(wins_by_country, labels=wins_by_country.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title("Number of Wins by Country")
    st.pyplot(fig)


elif page == "Goals Scored vs. Host Country":
    st.write("## Goals Scored⚽ vs. Host Country🏠 (1990-2022)")
    st.write('The host nation in a FIFA World Cup often plays a significant role in shaping the tournaments overall goals scored and performances. Host nations typically experience a "home advantage," where familiar surroundings, local support, and less travel fatigue can positively influence their results. This dynamic can lead to an increase in the number of goals scored in matches involving the host country. Additionally, the host nation’s matches can often set the tone for the tournament, influencing the flow of goals in other games. By analyzing the goals scored in each tournament alongside the performance of the host nation, we can gain a deeper understanding of how hosting the World Cup impacts scoring trends and overall competition dynamics.')
    st.subheader('Scatterplot of Host Nation vs Goals Scored During Tournament')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x="Host", y="Goals_Scored", data=df, ax=ax)
    for i, row in df.iterrows():
        ax.text(row['Host'], row['Goals_Scored'], str(row['Year']), color='black', ha='center', va='bottom')
    ax.set_xlabel("Host Country")
    ax.set_ylabel("Goals Scored")
    plt.xticks(rotation=45) 
    st.pyplot(fig)

elif page == "Overall Winners & Runners-Up":
    st.write("## Conclusion (🥇Overall Winners & 🥈Runners-Up)")
    st.write('The FIFA World Cup from 1990 to 2022 has showcased the evolution of football, reflecting changes in tactics, player development, and global competition. Over these tournaments, we have witnessed shifts in dominance among nations, with traditional powerhouses like Brazil, Germany, Italy and France maintaining their presence while new contenders emerged. The trends in goals scored highlight the increasing emphasis on attacking play, influenced by tactical advancements, rule changes, and the impact of technology such as VAR. Additionally, the role of host nations has remained crucial, often shaping the tournament’s atmosphere and sometimes influencing performances on the pitch. Ultimately, the World Cup remains the pinnacle of international football, bringing nations together in a display of skill, passion, and unpredictability. These tournaments have reinforced the sport’s ability to evolve while preserving its excitement, making each edition a unique and unforgettable spectacle.')
    
    st.write('I would like to shed a deeper light on the overall competition. Even though the research was mainly focused on 1990-2022 respectfully, the below chart shows the overall dominant teams since the tournament started in 1930.')
    teams_winners = {"Country": ["Brazil", "Germany", "Italy", "Argentina", "France", "Uruguay", "England", "Spain"],
                     "Titles Won": [5, 4, 4, 3, 2, 2, 1, 1]}
    df_winners = pd.DataFrame(teams_winners).sort_values(by="Titles Won", ascending=False)
    teams_runners_up = {"Country": ["Germany", "Argentina", "Netherlands", "Brazil", "Czechoslovakia", "Hungary", "Italy", "France", "Sweden", "Croatia"],
                        "Runner-Up Finishes": [4, 3, 3, 2, 2, 2, 2, 2, 1, 1]}
    df_runners_up = pd.DataFrame(teams_runners_up).sort_values(by="Runner-Up Finishes", ascending=False)
    
    def create_histogram(df, value_col, title, color):
        fig, ax = plt.subplots(figsize=(8, 5))
        y_pos = np.arange(len(df))
        ax.barh(y_pos, df[value_col], color=color, edgecolor="black", height=1.0)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(df["Country"])
        ax.set_xlabel(value_col)
        ax.set_ylabel("Country")
        ax.set_title(title)
        plt.gca().invert_yaxis()
        st.pyplot(fig)
    
    st.subheader("🥇**FIFA World Cup Titles Won 1930-2022**")
    st.write('Brazil stands out as the most successful team, winning the tournament five times, followed closely by Germany and Italy with four titles each. More recently, Argentina and France have cemented their status as football powerhouses, adding multiple trophies to their collections. Meanwhile, nations like Uruguay, England, and Spain have also made their mark with single victories.')
    create_histogram(df_winners, "Titles Won", "Histogram of FIFA World Cup Titles Won", "blue")
    
    st.subheader("🥈**FIFA World Cup Runner-Up Finishes**")
    st.write('On the other hand, the runner-up statistics highlight teams that have come close to glory but fallen just short. Germany leads in heartbreaks with four runner-up finishes, followed by Argentina and the Netherlands, each losing in three finals. Traditional footballing nations like Brazil, Italy, and France also feature prominently, proving their consistent competitiveness at the highest level. This historical data shows that while winning the World Cup requires exceptional talent and perseverance, reaching the final multiple times is an achievement in itself. Some nations have repeatedly showcased resilience, always remaining among the elite in world football.')
    create_histogram(df_runners_up, "Runner-Up Finishes", "Histogram of FIFA World Cup Runner-Up Finishes", "red")
