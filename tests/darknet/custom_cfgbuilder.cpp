#include<iostream>
#include<vector>
#include "tkdnn.h"
#include "test.h"
#include "DarknetParser.h"

int main(int argc, char** argv) {
    std::string path = std::string(argv[1]);
    std::string basename  = path.substr(path.find_last_of("/") + 1);

    std::string bin_path  = std::string("build/") + basename;
    std::string wgs_path  = ""; // use rand weights
    std::string cfg_path  = std::string(TKDNN_PATH) + "/" + argv[1];
    std::string name_path = std::string(TKDNN_PATH) + "/tests/darknet/names/coco.names";

    // parse darknet network
    tk::dnn::Network *net = tk::dnn::darknetParser(cfg_path, wgs_path, name_path);
    net->print();

    //convert network to tensorRT
    tk::dnn::NetworkRT *netRT = new tk::dnn::NetworkRT(net, net->getNetworkRTName(bin_path.c_str()));
    // tk::dnn::NetworkRT *netRT = new tk::dnn::NetworkRT(net, "");
    
    int test_num = atoi(argv[2]);
    int ret;
    for (int i=0; i<test_num;i++){
        ret = inferWithRandomInput(net, netRT);
    }
    net->releaseLayers();
    delete net;
    delete netRT;
    return ret;
}
