import sqlite3
import click
import datetime


@click.command()
def main():
    conn = sqlite3.connect("depression_survey.db")
    c = conn.cursor()
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS survey_results (
        id INTEGER PRIMARY KEY,
        date_taken TEXT,
        total_score INTEGER,
        q1 INTEGER,
        q2 INTEGER,
        q3 INTEGER,
        q4 INTEGER,
        q5 INTEGER,
        q6 INTEGER,
        q7 INTEGER,
        q8 INTEGER,
        q9 INTEGER,
        q10 INTEGER,
        q11 INTEGER,
        q12 INTEGER,
        q13 INTEGER,
        q14 INTEGER,
        q15 INTEGER,
        q16 INTEGER,
        q17 INTEGER,
        q18 INTEGER,
        q19 INTEGER,
        q20 INTEGER,
        q21 INTEGER,
        q22 INTEGER,
        q23 INTEGER,
        q24 INTEGER,
        q25 INTEGER
        
    )
    """
    )
    conn.commit()
    questions = [
        "Feeling sad or down in the dumps",
        "Feeling unhappy or blue",
        "Crying spells or tearfulness",
        "Feeling discouraged",
        "Feeling hopeless",
        "Low self-esteem",
        "Feeling worthless or inadequate",
        "Guilt or shame",
        "Criticizing yourself or blaming others",
        "Difficulty making decisions",
        "Loss of interest in family, friends or colleagues",
        "Loneliness",
        "Spending less time with family or friends",
        "Loss of motivation",
        "Loss of interest in work or other activities",
        "Avoiding work or other activities",
        "Loss of pleasure or satisfaction in life",
        "Feeling tired",
        "Difficulty sleeping or sleeping too much",
        "Decreased or increased appetite",
        "Loss of interest in sex",
        "Worrying about your health",
        "Do you have any suicidal thoughts?",
        "Would you like to end your life?",
        "Do you have a plan for harming yourself?",
    ]

    click.echo("Please answer the following questions:")
    click.echo("For each question, enter a number from 0 to 4:")
    click.echo("0 - Not at all")
    click.echo("1 - Somewhat")
    click.echo("2 - Moderately")
    click.echo("3 - A lot")
    click.echo("4 - Extremely")

    responses = []
    for i, question in enumerate(questions, start=1):
        response = click.prompt(f"{i}. {question} (0-4)", type=int, default=0)
        responses.append(response)

    total_score = sum(responses)
    click.echo(f"Total score: {total_score}")
    if 0 <= total_score <= 5:
        click.echo("No Depression")
    elif 6 <= total_score <= 10:
        click.echo("Normal but Happy")
    elif 11 <= total_score <= 25:
        click.echo("Mild Depression")
    elif 26 <= total_score <= 50:
        click.echo("Moderate Depression")
    elif 51 <= total_score <= 75:
        click.echo("Severe Depression")
    elif 76 <= total_score <= 100:
        click.echo("Extreme Depression")
    else:
        click.echo("Invalid score")

    date_taken = str(datetime.date.today())
    c.execute(
        """
        INSERT INTO survey_results (date_taken, total_score,q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
                                    q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (date_taken,) + (total_score,) + tuple(responses),
    )
    conn.commit()
    conn.close()
    click.echo("Survey results stored successfully!")


if __name__ == "__main__":
    main()
