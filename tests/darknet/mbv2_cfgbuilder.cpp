#include<iostream>
#include<vector>
#include "tkdnn.h"
#include "test.h"
#include "DarknetParser.h"

int main() {
    std::string bin_path  = "mbv2_cfgbuilder";
    std::string wgs_path  = ""; // use rand weights
    std::string cfg_path  = std::string(TKDNN_PATH) + "/tests/darknet/cfg/mobilenetv2_efficientnet_args_like.cfg";
    std::string name_path = std::string(TKDNN_PATH) + "/tests/darknet/names/coco.names";

    // parse darknet network
    tk::dnn::Network *net = tk::dnn::darknetParser(cfg_path, wgs_path, name_path);
    net->print();

    //convert network to tensorRT
    tk::dnn::NetworkRT *netRT = new tk::dnn::NetworkRT(net, net->getNetworkRTName(bin_path.c_str()));
    
    int test_num = 1000;
    int ret;
    for (int i=0; i<test_num;i++){
        ret = inferWithRandomInput(net, netRT);
    }
    net->releaseLayers();
    delete net;
    delete netRT;
    return ret;
}
