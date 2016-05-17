reset
set terminal png
set output "resnet_train.png"
set style data lines
set key right

# Training loss vs. training iterations
set title "Training loss vs. training iterations"
set xlabel "Training iterations"
set ylabel "Training loss"
plot "res.log.train" using 1:3 title "ResNet"

set output "resnet_test.png"
set style data lines
set key right

# Test accuracy vs. training time
set ylabel "Test accuracy"
set xlabel "Training time"
plot "res.log.test" using 2:3 title "ResNet"
