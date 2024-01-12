export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home
export PATH=/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home/bin:$PATH

#!/bin/sh
dir=$(dirname "$0")
java -cp "$dir./bin/h2-1.4.200.jar:$H2DRIVERS:$CLASSPATH" org.h2.tools.Console "$@" 