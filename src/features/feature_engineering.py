# Archivo: src/features/feature_engineering.py
# Creación de variables derivadas de trayectoria laboral

def create_loyalty_rate(df):

    df["LoyaltyRate"] = df["YearsAtCompany"] / df["TotalWorkingYears"].replace(0,1)

    return df


def create_stagnation_index(df):

    df["StagnationIndex"] = df["YearsSinceLastPromotion"] / df["YearsAtCompany"].replace(0,1)

    return df


def create_promotion_velocity(df):

    df["PromotionVelocity"] = df["TotalWorkingYears"] / df["JobLevel"].replace(0,1)

    return df


def create_career_mobility(df):

    df["CareerMobility"] = df["NumCompaniesWorked"] / df["TotalWorkingYears"].replace(0,1)

    return df
