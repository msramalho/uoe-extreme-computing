# call as sh meta-run.sh <TASK NO>
TASK=task$1
USER=s2004624
HOST=$USER@student.ssh.inf.ed.ac.uk

for i in "mapper.py" "mapper1.py" "mapper2.py" "reducer.py" "reducer1.py" "reducer2.py" "run.sh" "statistics.py" "movie.py"  "movie1.py"  "movie2.py" "combiner.py" "combiner1.py" "combiner2.py"
do
   FILE=$TASK/$i 
   if [ ! -f $FILE ]; then
      echo "$FILE not found."
   else
      echo "sending $FILE..."
      # convert CRLF to LF
      dos2unix $FILE
      # send file
      sshpass -f ".pass"  scp -r $FILE $HOST:/afs/inf.ed.ac.uk/user/s20/$USER/assignment/code/$FILE
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