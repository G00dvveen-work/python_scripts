today=$(date +"%d-%m-%Y")
cat //dc2erpapp15/Logs/Full/rphost_*/*.log //dc2erpapp16/Logs/Full/rphost_*/*.log |
awk -vORS= '{if(match($0, "^[0-9][0-9]:[0-9][0-9].[0-9]+-")) print "\n"$0; else print $0;}' |
perl -pe 's/\xef\xbb\xbf//g' |
grep -oP ",EXCP,.+Context=\K('.+?')" |
perl -pe "s/'//g" |
perl -pe "s/\t//g" |
gawk -F'\n' '{q[$1]=$1; c[$1]+=1} END {for (i in q) printf "%d\t%s \n", c[i], q[i]}' |
sort -rn |
#head -n 20 |
sed '1i\Count\tContext' > C:/Scripts/TechLogAnalysis/erp/result/excp_erp_$today.txt