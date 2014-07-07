module Main where
 
import           Data.ByteString.Lazy.Char8   (pack)
import qualified Data.ByteString.Lazy         as BL
 
header :: Int -> Int -> BL.ByteString
header columns rows = pack $ unlines ["P6","32 40","255"]

main :: IO ()
main = do
  contents <- BL.getContents
  BL.putStr $ header 3 2
