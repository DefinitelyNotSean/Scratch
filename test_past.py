from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, unix_timestamp, from_unixtime

spark = SparkSession.builder \
    .appName("Past Due Flag") \
    .getOrCreate()

# Assuming you have a DataFrame named df with columns control_risk_level and violation_open_timestamp

from pyspark.sql.functions import current_timestamp, datediff, expr

current_time = current_timestamp()

past_due_flag_expr = (
    when((col("control_risk_level") == "Critical") & (datediff(current_time, col("violation_open_timestamp")) * 24 > 4), True)
    .when((col("control_risk_level") == "High") & (datediff(current_time, col("violation_open_timestamp")) > 30), True)
    .when((col("control_risk_level") == "Medium") & (datediff(current_time, col("violation_open_timestamp")) > 60), True)
    .when((col("control_risk_level") == "Low") & (datediff(current_time, col("violation_open_timestamp")) > 90), True)
    .otherwise(False)
)

df_with_past_due_flag = df.withColumn("past_due_flag", past_due_flag_expr)

df_with_past_due_flag.show()





# or

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, unix_timestamp, from_unixtime, expr

spark = SparkSession.builder \
    .appName("Past Due Flag") \
    .getOrCreate()

# Assuming you have a DataFrame named df with columns control_risk_level and violation_open_timestamp

from pyspark.sql.functions import current_timestamp

current_time = current_timestamp()

past_due_flag_expr = (
    when((col("control_risk_level") == "Critical") & (current_time - expr("INTERVAL 4 HOURS") > col("violation_open_timestamp")), True)
    .when((col("control_risk_level") == "High") & (current_time - expr("INTERVAL 30 DAYS") > col("violation_open_timestamp")), True)
    .when((col("control_risk_level") == "Medium") & (current_time - expr("INTERVAL 60 DAYS") > col("violation_open_timestamp")), True)
    .when((col("control_risk_level") == "Low") & (current_time - expr("INTERVAL 90 DAYS") > col("violation_open_timestamp")), True)
    .otherwise(False)
)

df_with_past_due_flag = df.withColumn("past_due_flag", past_due_flag_expr)

df_with_past_due_flag.show()
