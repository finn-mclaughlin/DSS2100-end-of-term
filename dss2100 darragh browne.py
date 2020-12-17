{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "column_names = ['genotype', 'bout_length', 'fish']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "fish_data = pd.read_csv('C:/Users/35385/Pictures/2020-01/New folder/gandhi_et_al_bouts.csv', names = column_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "fish_data = fish_data[4:] # remove the first 4 lines of meta-data from the data#"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "bout_length_wt = fish_data[fish_data.genotype == 'wt'].bout_length #selecting only wild type fish from the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "bout_length_mut = fish_data[fish_data.genotype == 'mut'].bout_length #selecting only mutant type fish from the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    " = fish_data_mut[:1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bootstrap_replicate(data, func):                  #generates single bootstrap replicate\n",
    "    bootstrap_sample = np.random.choice(data, len(data))\n",
    "    return func(bootstrap_sample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "#compute the mean bout lengths of both groups\n",
    "mean_wt = np.mean(bout_length_wt['bout_length'])\n",
    "mean_mut = np.mean(bout_length_mut['bout_length'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'bout_length'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-109-fd782366e8d2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mbootstrap_wt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbootstrap_replicate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbout_length_wt\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'bout_length'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msize\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mbootstrap_mut\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbootstrap_replicate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbout_length_mut\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'bout_length'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msize\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\.conda\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    866\u001b[0m         \u001b[0mkey\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcom\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapply_if_callable\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    867\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 868\u001b[1;33m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    869\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    870\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mis_scalar\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\.conda\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mget_value\u001b[1;34m(self, series, key)\u001b[0m\n\u001b[0;32m   4373\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4374\u001b[0m             return self._engine.get_value(s, k,\n\u001b[1;32m-> 4375\u001b[1;33m                                           tz=getattr(series.dtype, 'tz', None))\n\u001b[0m\u001b[0;32m   4376\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4377\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m0\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mholds_integer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_boolean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_value\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_value\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas/_libs/index_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.index.Int64Engine._check_type\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'bout_length'"
     ]
    }
   ],
   "source": [
    "bootstrap_wt = bootstrap_replicate(bout_length_wt['bout_length'], np.mean, size = 1000)\n",
    "bootstrap_mut = bootstrap_replicate(bout_length_mut['bout_length'], np.mean, size = 1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'bootstrap_wt' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-65-f032fd8dbeb0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mconf_int_wt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpercentile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbootstrap_wt\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m2.5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m97.5\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mconf_int_mut\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpercentile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbootstrap_mut\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m2.5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m97.5\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'bootstrap_wt' is not defined"
     ]
    }
   ],
   "source": [
    "conf_int_wt = np.percentile(bootstrap_wt, [2.5, 97.5])\n",
    "conf_int_mut = np.percentile(bootstrap_mut, [2.5, 97.5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
