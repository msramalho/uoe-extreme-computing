# call as sh meta-run.sh <TASK NO>
TASK=task$1
USER=s2004624
HOST=$USER@student.ssh.inf.ed.ac.uk

for i in "mapper.py" "reducer.py" "run.sh"
do
   FILE=$TASK/$i 
   echo "$FILE"
   # convert CRLF to LF
   dos2unix $FILE
   # send file
   sshpass -f ".pass"  scp -r $FILE $HOST:/afs/inf.ed.ac.uk/user/s20/$USER/assignment/$FILE
   # convert LF back to CRLF
   unix2dos $FILE
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