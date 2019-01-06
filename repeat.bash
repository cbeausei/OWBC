while true
do
  python query_friends.py
  for i in {1..10}
  do
    python compute_table.py
    sleep 30
  done
done
