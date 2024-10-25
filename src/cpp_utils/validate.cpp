#include <iostream>
#include <fstream>
#include <string>

#include <glib.h>

using namespace std;

int main(int argc, const char* argv[]) {
    if (argc != 2) {
        std::cout << "\nUsage: check filename\n";
        return 0;
    }

    const char* test_file_path = argv[1];
    // Open the test file (contains UTF-8 encoded text)
    std::ifstream fs8;

    fs8.open(test_file_path);

    if (!fs8.is_open()) {
        std::cout << "Could not open " << test_file_path << std::endl;
    return 0;
    }

  string line;
  while (getline(fs8, line)) {
      const char *data = line.c_str();
      std::string s;

      for(char const *p = data, *pend = data; *pend != '\0'; p = pend + 1) {
        g_utf8_validate(p, -1, &pend);
        s.append(p, pend);
      }

    std::cout << s << std::endl;
  }
}
