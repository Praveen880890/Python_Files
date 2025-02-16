{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c983bf62-741c-4324-b737-f7f72296ed0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "n= [10,20,30,40,50]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "80da2de2-adbd-4ec3-9fb3-9ee715d36f78",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    count = 0\n",
    "    total = 0\n",
    "    for i in n:\n",
    "        count +=1\n",
    "        total +=i\n",
    "        # print(\"element is, \",i)\n",
    "        # print(\"\")\n",
    "        # print(\"sum till now, \",total)\n",
    "        # print(\"\")\n",
    "    print(\"total sum \",total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6c658b29-473d-44ba-b2b7-d88a81409e59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total sum  150\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ccd63de-5c37-482f-9c50-72c08cc59371",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
