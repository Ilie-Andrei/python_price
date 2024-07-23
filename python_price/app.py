import pandas as pd
import os


file_path = r"C:\Users\Andrei\Desktop\stock_price_data_files\LSE\GSK.csv"

data = pd.read_csv(file_path, header=None)

mean_price = data[2].mean()
std_dev_price = data[2].std()


outliers = data[(data[2] > (mean_price + 2 * std_dev_price)) |
                (data[2] < (mean_price - 2 * std_dev_price))]


print(f"\nInformation about the provided file")
print(f"\nThe average price value is: {mean_price}")
print(f"The standard deviation is: {std_dev_price}")


if not outliers.empty:

    for index, row in outliers.iterrows():
        print(f'''
Outliers:

Row\Column
{outliers}
''')


    base_path, original_filename = os.path.split(file_path)
    filename_without_ext, ext = os.path.splitext(original_filename)
    outliers_file_path = os.path.join(base_path, f"OUTLIERS_{filename_without_ext}{ext}")
    

    outliers.to_csv(outliers_file_path, index=False, header=False)

    print(f"Outliers have been saved to: {outliers_file_path}\n")

else:
    print("\nThere are no outliers in the provided file.\n")

