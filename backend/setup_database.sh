echo "CREATING DATABASE FOR SERVER..."

Result=`mysql -h "$DB_HOST" -u "$DB_USER" --skip-column-names -e "show databases like 'TaxCalculator'"`
if [ "$Result" != "TaxCalculator" ] 
then
  mysql -h "$DB_HOST" -u "$DB_USER" -e "CREATE DATABASE TaxCalculator"
  mysql -h "$DB_HOST" -u "$DB_USER" TaxCalculator < TaxCalculator.sql
fi


echo "FINISHED CREATING DATABASE FOR SEVER"
