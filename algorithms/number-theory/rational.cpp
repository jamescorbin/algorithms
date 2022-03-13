#include <string>
#include <iostream>
#include "euclid-algorithm.h"

class Rational {
		private:
				int num;
				int den;
				void reduce() {
						if (den < 0) {
								den = -den;
								num = -num;
						}
						int d = euclid(num, den);
						num = num / d;
						den = den / d;
				}

		public:
				Rational() {
						num = 1;
						den = 1;
				}
				
				Rational(int n, int d) {
					num = n;
					den = d;
					this->reduce();
				}

				Rational(const Rational& q) {
					num = q.num;
					den = q.den;
					this->reduce();
				}

				int add(const Rational& x) {
						num = num * x.den + x.num * den;
						den = den * x.den;
						this->reduce();
						return 0;
				}

				int diff(const Rational& x) {
						num = num * x.den - x.num * den;
						den = den * x.den;
						this->reduce();
						return 0;
				}

				int mult(const Rational& x) {
						num = num * x.num;
						den = den * x.den;
						this->reduce();
						return 0;
				}

				int div(const Rational& x) {
						num = num * x.den;
						den = den * x.num;
						this->reduce();
						return 0;
				}

				std::string to_string() {
						const char* slash = "/";
						std::string s = std::to_string(num) 
								+ slash + std::to_string(den);
						return s;
				}

				Rational operator+(const Rational& x) {
						Rational q(x);
						q.add(*this);
						return q;
				}

				Rational operator-(const Rational& x) {
						Rational q(x);
						q.diff(*this);
						return q;
				}

				Rational operator*(const Rational& x) {
						Rational q(x);
						q.mult(*this);
						return q;
				}

				Rational operator/(const Rational& x) {
						Rational q(x);
						q.div(*this);
						return q;
				}
};






