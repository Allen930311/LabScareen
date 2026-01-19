import csv
import os

# 這是您的完整藥品清單 (我已經將資料整理好)
data = [
    # (CAS, 上層藥品名稱, 廠牌, 數量)
    ("199926-39-1", "Chelidamic acid monohydrate", "TCI", "25 G*2"),
    ("502-44-3", "ε-Caprolactone", "ACROS", "1 KG + 250 G"),
    ("105946-82-5", "4-Bromo-4'-iodo-1,1'-biphenyl", "NOVA", "25 G"),  # <--- 這行就是原本報錯的兇手
    ("7311-63-9", "5-Bromo-2-thiophenecarboxylic acid", "MATRIX", "25 G"),
    ("402-43-7", "4-Bromobenzotrifluoride", "MATRIX", "100 G"),
    ("13149-00-3", "cis-1,2-Cyclohexanedicarboxylic anhydride", "ALDRICH", "100 G"),
    ("124-42-5", "Acetamidine hydrochloride", "ACROS", "100 G*2"),
    ("56-84-8", "L-Aspartic acid", "MP BIOMEDICALS", "100 G"),
    ("700-58-3", "2-Adamantanone", "MERCK", "25 G"),
    ("119-67-5", "2-Carboxybenzaldehyde", "ACROS", "100 G"),
    ("100-66-3", "Anisole", "LANCASTER", "500 G"),
    ("4595-60-2", "2-Bromopyrimidine", "ALFA", "25 G"),
    ("4627-22-9", "Bis(4-tert-butylphenyl)amine", "TCI", "25 G"),
    ("6326-79-0", "6-Bromoisatin", "MATRIX、TCI", "25 G*2"),
    ("100-48-1", "4-Cyanopyridine", "Acros", "100 G"),
    ("623-00-7", "4-Bromobenzonitrile", "ALFA", "50 G"),
    ("5344-90-1", "2-Aminobenzyl alcohol", "ACROS", "25 G*3"),
    ("110-65-6", "2-Butyne-1,4-diol", "ACROS", "250 G"),
    ("99-05-8", "3-Aminobenzoic acid", "ACROS", "100 G"),
    ("120-80-9", "1,2-Dihydroxybenzene", "ACROS", "500 G"),
    ("150-13-0", "4-Aminobenzoic acid", "Acros", "250 G"),
    ("281-23-2", "Adamantane", "Acros", "100 G"),
    ("5872-08-2", "Camphor-10-sulfonic acid (β)", "LANCASTER", "100 G"),
    ("6280-88-2", "4-Chloro-2-nitrobenzoic acid", "TCI+LANCASTER+ACROS", "25 G + 100 G*2"),
    ("104-63-2", "2-Benzylaminoethanol", "ACROS", "100 mL"),
    ("7379-35-3", "4-Chloropyridine hydrochloride", "ACROS", "25 G"),
    ("100-70-9", "2-cyanopyridine", "ACROS", "100 G"),
    ("137-07-5", "2-Aminothiophenol", "ACROS", "100 G"),
    ("67567-26-4", "4-Bromo-2,6-difluoroaniline", "MATRIX", "100 G"),
    ("7790-94-5", "Chlorosulfonic acid", "LANCASTER", "100 G"),
    ("43076-61-5", "4′-tert-Butyl-4-chlorobutyrophenone", "ACROS", "50 G"),
    ("589-87-7", "1-Bromo-4-iodobenzene", "NOVA", "100 G*2"),
    ("464-49-3", "D-Camphor", "ACROS", "100 G"),
    ("502-42-1", "Cycloheptanone", "ACROS", "100 G"),
    ("1885-29-6", "2-Aminobenzonitrile", "ACROS*3+LANCASTER", "250 G + 100 G*3"),
    ("586-76-5", "4-Bromobenzoic acid", "ACROS", "25 G*2"),
    ("95-47-6", "o-Xylene", "NOVA", "500 G"),
    ("372-09-8", "Cyanoacetic acid", "ACROS", "250 G + 分裝罐"),
    ("97-00-7", "1-chloro-2,4-dinitrobenzene", "Alfa", "100 G"),
    ("118-75-2", "Chloranil", "NOVA、Acros", "100 G*2"),
    ("87-82-1", "hexabromobenzene", "NOVA", "100 G"),
    ("488-48-2", "bromanil", "NOVA", "5 G"),
    ("1122-62-9", "2-Acetylpyridine", "NOVA", "25 G"),
    ("1197-55-3", "4-Aminophenylacetic acid", "NOVA", "100 G"),
    ("140-10-3", "trans-Cinnamic acid", "ACROS", "5 G"),
    ("13223-25-1", "2-Chloro-4,6-dimethoxypyrimidine", "FLUKA", "25 G"),
    ("4224-70-8", "6-Bromohexanoic acid", "ACROS", "25 G"),
    ("13472-85-0", "5-Bromo-2-methoxypyridine", "MATRIX", "25 G"),
    ("1556-09-8", "Bromocyclooctane", "ALFA", "25 G"),
    ("2404-35-5", "Bromocycloheptane", "ACROS", "25 G"),
    ("1199-69-5", "4-(2-Amino-ethyl)-Benzoic acid", "ALDRICH", "5 G"),
    ("6311-35-9", "2-Bromo-5-pyridinecarboxylic acid", "MATRIX", "25 G"),
    ("3510-66-5", "2-Bromo-5-methylpyridine", "ALFA", "25 G*2"),
    ("364-73-8", "4-Bromo-1-fluoro-2-nitrobenzene", "MATRIX", "25 G*2"),
    ("3312-04-7", "4-Chloro-1,1-bis(p-fluorophenyl)butane", "ACROS", "25 G"),
    ("1575-37-7", "4-Bromo-1,2-diaminobenzene", "ALFA", "5G"),
    ("4595-59-9", "5-Bromopyrimidine", "ACROS", "25 G"),
    ("2623-87-2", "4-Bromobutyric acid", "ACROS", "25 G")
]

# 設定正確的中文欄位名稱
header = ['CAS', '上層藥品名稱', '廠牌', '數量']
filename = "Clean_Inventory.csv"

try:
    # newline='' 避免 Windows 產生多餘空行
    # encoding='utf-8-sig' 讓 Excel 開啟時中文不會亂碼
    # quoting=csv.QUOTE_MINIMAL 這是關鍵！它會自動幫有逗號的欄位加上雙引號
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)  # 寫入標題
        writer.writerows(data)   # 寫入資料
        
    print(f"✅ 修復完成！")
    print(f"已產生正確的檔案：{os.path.abspath(filename)}")
    print("請重新執行掃描程式，並選擇這個 'Clean_Inventory.csv' 檔案。")

except Exception as e:
    print(f"❌ 錯誤：{e}")
    