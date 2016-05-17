reset
set terminal png
set output "lenet_train.png"
set style data lines
set key right

# Training loss vs. training iterations
set title "Training loss vs. training iterations"
set xlabel "Training iterations"
set ylabel "Training loss"
plot "lenet.log.train" using 1:3 title "LeNet"

set output "lenet_test.png"
set style data lines
set key right

# Test accuracy vs. training time
set ylabel "Test accuracy"
set xlabel "Training time"
plot "lenet.log.test" using 2:3 title "LeNet"
