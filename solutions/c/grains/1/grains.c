#include "grains.h"
#include "math.h"
uint64_t square(uint8_t index){
    if (index == 1){
        return 1;
    }
    if (index == 2){
        return 2;
    }
    return pow(2,(index-1));
}
uint64_t total(void){
    uint64_t acu = 0;
    for (uint8_t i = 1; i <= 64; i++) {
        acu += square(i);
    }
    return acu;
}