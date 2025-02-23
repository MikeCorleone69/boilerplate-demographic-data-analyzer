import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load the dataset
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race are represented?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    bachelors_percentage = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage of people with advanced education (>50K)
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education]['salary'] == '>50K').mean() * 100, 1)

    # 5. Percentage of people without advanced education (>50K)
    lower_education_rich = round((df[~advanced_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. Minimum work hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of min-hour workers earning >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. Country with highest percentage of >50K earners
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    country_rich_percentage = (country_salary / country_count * 100).dropna()
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Most common occupation in India among >50K earners
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Print the results if print_data is True
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", bachelors_percentage)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among min workers:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    # Return the results as a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': bachelors_percentage,  # ✅ Correct key name
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
