# call as sh meta-run.sh <TASK NO>
TASK=task$1
USER=s2004624
HOST=$USER@student.ssh.inf.ed.ac.uk

for i in "mapper.py" "mapper_1.py" "mapper_2.py" "reducer.py" "reducer_1.py" "reducer_2.py" "run.sh" "statistics.py" "combiner.py" "combiner_1.py" "combiner_2.py"
do
   FILE=$TASK/$i 
   if [ ! -f $FILE ]; then
      echo "$FILE not found."
   else
      echo "sending $FILE..."
      # convert CRLF to LF
      dos2unix $FILE
      # send file
      sshpass -f ".pass"  scp -r $FILE $HOST:/afs/inf.ed.ac.uk/user/s20/$USER/assignment/$FILE
      # convert LF back to CRLF
      unix2dos $FILE
   fi
done

# ssh login and execute commands
sshpass -f ".pass" ssh -tt $HOST /bin/bash << EOF
	ssh hadoop.exc
      cd ./assignment/$TASK
      chmod a+x *.py run.sh
      sh run.sh
      exit
   exit
EOF