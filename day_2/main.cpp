//
// Created by Francis on 2/12/2025.
//

#include <fstream>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

std::string sample_file_path = "sample.txt";


int main()
{
    std::ifstream inputFile(sample_file_path, std::ios::in);
    std::string strInput(std::istreambuf_iterator<char>{inputFile}, {});
    std::string_view strInputView{strInput};
    std::vector<std::string_view> items;
    size_t commaPos = std::string::npos;
    size_t startPos = 0;

    do
    {
        commaPos = strInput.find(',', startPos);
        if (commaPos != std::string::npos)
        {
            items.push_back(strInputView.substr(startPos, commaPos - startPos));
            startPos = commaPos+1;
            if (startPos == strInput.size()) break;
        }
    }
    while (std::string::npos != commaPos);



    std::cout << items.size() << std::endl;

}